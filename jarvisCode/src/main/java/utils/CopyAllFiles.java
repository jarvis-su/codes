package utils;

import java.io.BufferedInputStream;
import java.io.BufferedOutputStream;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.util.List;
import java.util.Vector;

import javax.swing.JOptionPane;

public class CopyAllFiles {

	/**
	 * @param args
	 */
	private static int filesToBeCopied = -1;
	// 要创建的线程数
	private static int THREAD_COUNT = 4;
	private static int n = 0;
	private static String sourcePath;
	private static String destPath;

	public static void main(String[] args) {
		// TODO 自动生成的方法存根
		// 线程池
		List<File> pool = new Vector<File>();
		setFilePath();
		// 设置线程池，存放源目录的所有文件
		int totalFiles = setCopiedFiles(sourcePath, pool);
		filesToBeCopied = totalFiles;
		System.out.println("total files ： " + filesToBeCopied);
		// 建立和运行线程
		Thread[] threads = new Thread[THREAD_COUNT];
		for (int i = 0; i < threads.length; i++) {
			threads[i] = new CopyThread(pool);
			threads[i].start();
		}
		// 安全起见，手动唤醒所有线程
		for (int i = 0; i < threads.length; i++) {
			threads[i].interrupt();
		}
	}

	// 递归的方式读取文件
	private static int setCopiedFiles(String path, List<File> pool) {
		File sourceFile = new File(path);
		if (sourceFile.isFile()) {
			// 同步线程池，并唤醒所有等待的线程
			synchronized (pool) {
				pool.add(sourceFile);
				pool.notifyAll();
				n++;
			}
		} else {
			File[] files = sourceFile.listFiles();
			for (int i = 0; i < files.length; i++) {
				String tempString = files[i].getAbsolutePath();
				setCopiedFiles(tempString, pool);
			}
		}
		return n;
	}

	public static int getFilesToBeCopied() {
		return filesToBeCopied;
	}

	// 设置目录
	private static void setFilePath() {
		String temp = JOptionPane
				.showInputDialog("Input Source File Path(like C:\\\\projects) :");
		sourcePath = temp;
		temp = JOptionPane
				.showInputDialog("Input Target File Path(like C:\\\\projects) :");
		destPath = temp;
	}

	public static String getSourceFilePath() {
		return sourcePath;
	}

	public static String getTargetFilePath() {
		return destPath;
	}
}

class CopyThread extends Thread {
	private static int copiedFiles = 0;
	private List<File> pool;

	public CopyThread(List<File> pool) {
		this.pool = pool;
	}

	public void run() {
		File input = null;
		while (copiedFiles != CopyAllFiles.getFilesToBeCopied()) {
			// 当线程池为空时，等待
			synchronized (pool) {
				while (pool.isEmpty()) {
					if (copiedFiles == CopyAllFiles.getFilesToBeCopied())
						return;
					try {
						pool.wait();
					} catch (InterruptedException e) {
						// TODO 自动生成的 catch 块
						e.printStackTrace();
					}
				}
				input = (File) pool.remove(pool.size() - 1);
				copiedFilesIncrement();
			}
			// 文件复制
			try {
				FileInputStream in = new FileInputStream(input);
				BufferedInputStream bi = new BufferedInputStream(in);
				String targetPath = CopyAllFiles.getTargetFilePath();
				File destFile = new File(targetPath, input.getName());
				FileOutputStream out = new FileOutputStream(destFile);
				BufferedOutputStream bo = new BufferedOutputStream(out);
				int b;
				while ((b = bi.read()) != -1) {
					bo.write(b);
				}
				bo.flush();
				bi.close();
				in.close();
				out.close();
				bo.close();
			} catch (Exception e) {
				// TODO: handle exception
				e.printStackTrace();
			}
		}
		System.exit(0);
	}

	private static synchronized void copiedFilesIncrement() {
		copiedFiles++;
	}
}
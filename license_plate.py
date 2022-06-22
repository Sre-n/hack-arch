def debug_imshow(self, title, image, waitKey=False):
		if self.debug:
			cv2.imshow(title, image)
			if waitKey:
				cv2.waitKey(0)

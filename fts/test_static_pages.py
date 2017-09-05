from functional_tests import FunctionalTest, ROOT

class TestHomePage(FunctionalTest):

	def test_can_view_home_page(self):

		#someone opens his browser and goes to the home-page of the tukker app
		self.browser.get(ROOT + '/tukker')

		#he's looking at the homepage and sees the Heading "Messages with 300 Chars"
		body = self.browser.find_element_by_tag_name('body')
		self.assertIn('Messages With 300 Chars', body.text)

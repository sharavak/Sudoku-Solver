module.exports = {
	globDirectory: './',
	globPatterns: [
		'**/*.{jpg,png,js,html,css}'
	],
	swDest: 'sw.js',
	ignoreURLParametersMatching: [
		/^utm_/,
		/^fbclid$/
	]
};
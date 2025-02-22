module.exports = {
	globDirectory: '.',
	globPatterns: [
		'**/*.{jpg,png,txt,json,js,html,md,css}'
	],
	swDest: 'sw.js',
	ignoreURLParametersMatching: [
		/^utm_/,
		/^fbclid$/,
		/^q/
	]
};
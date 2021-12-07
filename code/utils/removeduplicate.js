fs = require('fs')

v = ['a', 'a', 'b', 'b', 'c']

filtered = [...new Set(v)]

fs.writeFile('filtered.js', JSON.stringify(uniqNegative), function (err) {
  if (err) return console.log(err)
})

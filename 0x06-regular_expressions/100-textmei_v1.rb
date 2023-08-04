#!/usr/bin/env ruby
# puts ARGV[0].scan(/\+\d{11}/).join
# puts ARGV[0].scan(/-*\d:-*\d:-*\d:-*\d:-*\d/).join


sender = ARGV[0].scan(/\[from:\+?\w*\]/).join
receiver = ARGV[0].scan(/\[to:\+?\w*\]/).join
flags = ARGV[0].scan(/\[flags:-?\d:-?\d:-?\d:-?\d:-?\d\]/).join


sender = sender.scan(/(?<=.{6})\w*[^\+\[\]]/).join
receiver = receiver.scan(/(?<=.{4})\w*[^\+\[\]]/).join
flags = flags.scan(/(?<=.{7}).*[^\[\]]/).join
# sender = (?<=.{6}).*[^\[\]]

#sender = ARGV[0].scan(/\[from:\+?\w*\]/).join
#receiver = ARGV[0].scan(/\[to:\+?\w*\]/).join
#flags = ARGV[0].scan(/\[flags:-?\d:-?\d:-?\d:-?\d:-?\d\]/).join

puts "#{sender},#{receiver},#{flags}"
# puts ARGV[0].scan(/^\[to.*\]$/).join
# puts ARGV[0].scan(/^\[flags.*\]$/).join
# puts ARGV[0].scan(/\[flags:-?\d:-?\d:-?\d:-?\d:-?\d\}/).join

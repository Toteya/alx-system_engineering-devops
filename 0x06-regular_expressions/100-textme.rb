#!/usr/bin/env ruby

sender = ARGV[0].scan(/\[from:\+?\w*\]/).join
receiver = ARGV[0].scan(/\[to:\+?\w*\]/).join
flags = ARGV[0].scan(/\[flags:-?\d:-?\d:-?\d:-?\d:-?\d\]/).join

sender = sender.scan(/(?<=.{6})\w*[^\[\]]/).join
receiver = receiver.scan(/(?<=.{4})\w*[^\[\]]/).join
flags = flags.scan(/(?<=.{7}).*[^\[\]]/).join

puts "#{sender},#{receiver},#{flags}"

-- Get fibbonacii numbers not exceeding maxfib
fibs :: Int -> [Int]
fibs maxfib = fibsa 2 1 maxfib [2, 1]

fibsa :: Int -> Int -> Int -> [Int] -> [Int]
fibsa n1 n2 maxfib accum =  if curfib > maxfib
                            then accum
                            else fibsa curfib n1 maxfib (curfib:accum)
                        where curfib = n1 + n2

iseven x = (x `mod` 2) == 0

main = do
        let f4m = fibs 4000000
        let f4meven = filter iseven f4m        
        putStrLn $ show $ f4meven
        putStrLn $ show $ sum f4meven
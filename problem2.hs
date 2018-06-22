fiblist n = reverse $ fiblist' n
    where
        fiblist' 1 = [1]
        fiblist' 2 = [1, 1]
        fiblist' n = let fib1:fib2:fiblst = fiblist' (n - 1)
                         fibcur = fib1 + fib2
                     in fibcur:fib1:fib2:fiblst

main = do
        putStrLn $ show $ (fiblist 12)
data State = Null
          |  Node String State State

valid :: State -> Bool
valid state = case state of
                Null              -> undefined
                Node string _ _   -> null string

match :: String -> String -> [Int]
match pattern = map fst . filter (valid . snd) . scanl step (0, root)
                where
                    step (length, state) token = (length+1, op state token)
                    op state token = case state of
                                       Null            -> root
                                       Node [] left _  -> op left token
                                       Node (x:xs) left right -> if x/=token then op left token else right

                    root = build Null pattern
                    build left pattern = case pattern of
                                              []  -> Node [] left Null
                                              x:xs -> Node pattern left (build (op left x) xs)

main = do
        pattern <- getLine
        text    <- getLine
        print $ match pattern text
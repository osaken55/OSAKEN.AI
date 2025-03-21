```mermaid
flowchart TD

    %% --- カラー定義（クラス） ---
    classDef pastelPink fill:#FFC0CB,stroke:#FF99CC,color:#000,stroke-width:2px
    classDef pastelGreen fill:#CCFFCC,stroke:#99CC99,color:#000,stroke-width:px
    classDef pastelBlue fill:#ADD8E6,stroke:#87CEEB,color:#000,stroke-width:2px
    classDef pastelYellow fill:#FFFFE0,stroke:#F0E68C,color:#000,stroke-width:2px
    classDef pastelOrange fill:#FFDAB9,stroke:#FFA07A,color:#000,stroke-width:2px
    classDef pastelLavender fill:#E6E6FA,stroke:#D8BFD8,color:#000,stroke-width:2px

    %% --- フロー構造 ---
    A["GORA/GDOで予約<br>⛳️🏌️‍♂️"] --> B["初来場でアンケート<br>＆LINE登録 📱"]

    B ==> C["UTAGEでデータ管理<br>👩‍💻🗂"]

    C --> D["自動ステップ配信<br>(メール＆LINE) 🚀"]

    D --> E{"再来場の有無？<br>(分岐) 🤔"}

    E -->|再来場アリ🏌️‍♀️| F["リピート顧客へ<br>会員権案内 💌"]
    E -->|再来場ナシ👀| G["追客フォロー<br>クーポン送付 🎟"]

    F --> H{"年間/法人会員<br>お得プランの提案 🤑🎉"}

    H -->|社長に電話👩‍💼📞| I["『小島社長、<br>ありがとうございます！』🎊"]

    G ==> D

    I ==> J(("完了 ��"))

    %% スタイルの適用
    A:::pastelPink
    B:::pastelGreen
    C:::pastelBlue
    D:::pastelLavender
    E:::pastelYellow
    F:::pastelGreen
    G:::pastelOrange
    H:::pastelPink
    I:::pastelBlue
    J:::pastelGreen
    

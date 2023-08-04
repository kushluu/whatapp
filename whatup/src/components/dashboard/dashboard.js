import React, { useEffect, useState } from 'react';
import './dashboard.css'
import axios from 'axios'
const Dashboard = () => {
    const [chatuser, setchatuser] = useState()
    const [ischatopen, setischatopen] = useState(false)
    const [messages, setmessages] = useState([])
    //  socket.onmessage = (event) => {
    //     const newMessage = event.data;
    //     setmessages(prevMessages => [...prevMessages, newMessage]);
    //   };
    //   socket.onclose = () => {
    //     console.log('WebSocket connection closed');
    //   };

    // const data =  [
    //     {
    //         name: 'John',
    //         last_seen: '8:39',
    //         last_message: 'hello',
    //         profile: 'p1'
    //     }
    //     ,
    //     {
    //         name: 'ram ',
    //         last_seen: '3:30',
    //         last_message: 'hey',
    //         profile: 'p2'
    //     },
    //     {
    //         name: 'ravi  ',
    //         last_seen: '4:30',
    //         last_message: 'hi',
    //         profile: 'p2'
    //     }
    // ]
    const [isFlipped, setIsFlipped] = useState(true);

    const handleFlip = () => {
        console.log(isFlipped)
        setIsFlipped(!isFlipped);
    };
    let [usersdata, setusersdata] = useState([])
    const openchat = (user) => {
        setischatopen(true)
        setchatuser(user)
        console.log(chatuser)

    }

    const getusersdata = () => {
        setusersdata([
            {
                name: 'John',
                last_seen: '8:39',
                last_message: 'hello',
                profile: 'p1.jpg'
            }
            ,
            {
                name: 'ram ',
                last_seen: '3:30',
                last_message: 'hey',
                profile: 'p2.jpg'
            },
            {
                name: 'ravi  ',
                last_seen: '4:30',
                last_message: 'hi',
                profile: 'p2.jpg'
            }
        ]
        )

        // axios.get('http://127.0.0.1:8001/user/login')
        //   .then((response) => {

        //   })
        //   .catch((error) => {
        //     console.error('POST Error:', error);
        //   });

    };
    useEffect(() => getusersdata(), [])

    return (
        <>

            <div className='main'>
                <div className={`flip-card chats-container ${isFlipped ? 'flip-card-inner':' '} `}>
                    <div className="flip-card-inner">
                        <div className="flip-card-front front">
                            <div>
                                <input type='search'></input>
                                <button className='add-btn' onClick={handleFlip}>Add</button>

                            </div>
                            {usersdata.map((user, index) => (
                                <>
                                    <div key={index} className='user-container' onClick={() => openchat(user)}>
                                        <div className='profilepicdiv'>
                                            <img src={user.profile} alt="Profile" />
                                        </div>
                                        <div className='user-profile'>
                                            <h2>{user.name}</h2>
                                        </div>

                                    </div>
                                    <hr></hr>
                                </>
                            ))}

                        </div>
                        <div className="flip-card-back back">
                            <div>
                                <input type='search'></input>
                                <button onClick={handleFlip}> back</button>
                            </div>
                        </div>
                    </div>
                </div>
                <div className='chat-container'>
                    {chatuser?.name}
                </div>
                
            </div></>




        // <div className='main'>

        //     <div className={`chats-container $ {isFlipped ? 'flipped':' '}`}>
        //         <div className="flipper">
        //             <div className="front">
        //                 <div>
        //                     <input type='search'></input>
        //                     <button className='add-btn' onClick={handleFlip}>Add</button>

        //                 </div>
        //                 {usersdata.map((user, index) => (
        //                     <>
        //                         <div key={index} className='user-container' onClick={() => openchat(user)}>
        //                             {index}
        //                             <div className='profilepicdiv'>
        //                                 <img src={user.profile} alt="Profile" />
        //                             </div>
        //                             <div className='user-profile'>
        //                                 <h2>{user.name}</h2>
        //                             </div>

        //                         </div>
        //                         <hr></hr>
        //                     </>
        //                 ))}
        //             </div>
        //             <div className="back">
        //                 <div>
        //                     <input type='search'></input>
        //                     <button onClick={handleFlip}> back</button>
        //                 </div>
        //             </div>
        //         </div>
        //     </div>
        //     <div className='chat-container'>
        //         .
        //         {chatuser?.name}
        //     </div>


        // </div>

    );


}


export default Dashboard;

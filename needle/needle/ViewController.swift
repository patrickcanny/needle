//
//  ViewController.swift
//  needle
//
//  Created by Patrick Canny on 11/3/17.
//  Copyright © 2017 Patrick Canny. All rights reserved.
//

import UIKit

class ViewController: UIViewController {
    var auth = SPTAuth.defaultInstance()!
    var session:SPTSession!
    
    var player: SPTAudioStreamingController?
    var loginUrl: URL?
    
    func setup(){
        SPTAuth.defaultInstance().clientID = "76dc1bdb68414251b6ed9380f7b7b1be"
        SPTAuth.defaultInstance().redirectURL = URL(string: "needle://returnAfterLogin")
        SPTAuth.defaultInstance().requestedScopes = [SPTAuthStreamingScope, SPTAuthPlaylistReadPrivateScope, SPTAuthPlaylistModifyPublicScope, SPTAuthPlaylistModifyPrivateScope]
        loginUrl = SPTAuth.defaultInstance().spotifyWebAuthenticationURL()
        
        
        
    }

    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view, typically from a nib.
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }


}


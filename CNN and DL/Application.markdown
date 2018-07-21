
Machine Learning Mastery

Start Here       Blog       Books       FAQ       About       Contact

Need help with Deep Learning? Take the FREE Mini-Course
8 Inspirational Applications of Deep Learning
By Jason Brownlee on July 14, 2016 in Deep Learning

It is hyperbole to say deep learning is achieving state-of-the-art results across a range of difficult problem domains. A fact, but also hyperbole.

There is a lot of excitement around artificial intelligence, machine learning and deep learning at the moment. It is also an amazing opportunity to get on on the ground floor of some really powerful tech.

I try hard to convince friends, colleagues and students to get started in deep learning and bold statements like the above are not enough. It requires stories, pictures and research papers.

In this post you will discover amazing and recent applications of deep learning that will inspire you to get started in deep learning.

Getting started in deep learning does not have to mean go and study the equations for the next 2-3 years, it could mean download Keras and start running your first model in 5 minutes flat. Start applied deep learning. Build things. Get excited and turn it into code and systems.

I have been wanting to write this post for a while. Let’s get started.
Inspirational Applications of Deep Learning

Inspirational Applications of Deep Learning
Photo by Nick Kenrick, some rights reserved.
Overview

Below is the list of the specific examples we are going to look at in this post.

Not all of the examples are technology that is ready for prime time, but guaranteed, they are all examples that will get you excited.

Some are examples that seem ho hum if you have been around the field for a while. In the broader context, they are not ho hum. Not at all.

Frankly, to an old AI hacker like me, some of these examples are a slap in the face. Problems that I simply did not think we could tackle for decades, if at all.

I’ve focused on visual examples because we can look at screenshots and videos to immediately get an idea of what the algorithm is doing, but there are just as many if not more examples in natural language with text and audio data that are not listed.

Here’s the list:

    Colorization of Black and White Images.
    Adding Sounds To Silent Movies.
    Automatic Machine Translation.
    Object Classification in Photographs.
    Automatic Handwriting Generation.
    Character Text Generation.
    Image Caption Generation.
    Automatic Game Playing.

Need help with Deep Learning in Python?

Take my free 2-week email course and discover MLPs, CNNs and LSTMs (with code).

Click to sign-up now and also get a free PDF Ebook version of the course.

Start Your FREE Mini-Course Now!

1. Automatic Colorization of Black and White Images

Image colorization is the problem of adding color to black and white photographs.

Traditionally this was done by hand with human effort because it is such a difficult task.

Deep learning can be used to use the objects and their context within the photograph to color the image, much like a human operator might approach the problem.

A visual and highly impressive feat.

This capability leverages of the high quality and very large convolutional neural networks trained for ImageNet and co-opted for the problem of image colorization.

Generally the approach involves the use of very large convolutional neural networks and supervised layers that recreate the image with the addition of color.
Colorization of Black and White Photographs

Colorization of Black and White Photographs
Image taken from Richard Zhang, Phillip Isola and Alexei A. Efros.

Impressively, the same approach can be used to colorize still frames of black and white movies

Further Reading

    Automatic Colorization
    Automatic Colorization of Grayscale Images

Papers

    Deep Colorization [pdf], 2015
    Colorful Image Colorization [pdf] (website), 2016
    Learning Representations for Automatic Colorization [pdf] (website), 2016
    Image Colorization with Deep Convolutional Neural Networks [pdf], 2016

2. Automatically Adding Sounds To Silent Movies

In this task the system must synthesize sounds to match a silent video.

The system is trained using 1000 examples of video with sound of a drum stick striking different surfaces and creating different sounds. A deep learning model associates the video frames with a database of pre-rerecorded sounds in order to select a sound to play that best matches what is happening in the scene.

The system was then evaluated using a turing-test like setup where humans had to determine which video had the real or the fake (synthesized) sounds.

A very cool application of both convolutional neural networks and LSTM recurrent neural networks.

Further Reading

    Artificial intelligence produces realistic sounds that fool humans
    Machines can generate sound effects that fool humans

Papers

    Visually Indicated Sounds (webpage), 2015

3. Automatic Machine Translation

This is a task where given words, phrase or sentence in one language, automatically translate it into another language.

Automatic machine translation has been around for a long time, but deep learning is achieving top results in two specific areas:

    Automatic Translation of Text.
    Automatic Translation of Images.

Text translation can be performed without any preprocessing of the sequence, allowing the algorithm to learn the dependencies between words and their mapping to a new language. Stacked networks of large LSTM recurrent neural networks are used to perform this translation.

As you would expect, convolutional neural networks are used to identify images that have letters and where the letters are in the scene. Once identified, they can be turned into text, translated and the image recreated with the translated text. This is often called instant visual translation.
Instant Visual Translation

Instant Visual Translation
Example of instant visual translation, taken from the Google Blog.
Further Reading

It’s hard to find good resources for this example, if you know any, can you leave a comment.

    How Google Translate squeezes deep learning onto a phone

Papers

    Sequence to Sequence Learning with Neural Networks [pdf], 2014
    Learning Phrase Representations using RNN Encoder-Decoder for Statistical Machine Translation [pdf], 2014
    Deep Neural Networks in Machine Translation: An Overview [pdf], 2015

4. Object Classification and Detection in Photographs

This task requires the classification of objects within a photograph as one of a set of previously known objects.

State-of-the-art results have been achieved on benchmark examples of this problem using very large convolutional neural networks. A breakthrough in this problem by Alex Krizhevsky et al. results on the ImageNet classification problem called AlexNet.
Example of Object Classification

Example of Object Classification
Taken from ImageNet Classification with Deep Convolutional Neural Networks

A more complex variation of this task called object detection involves specifically identifying one or more objects within the scene of the photograph and drawing a box around them.
Automatic Object Detection

Example of Object Detection within Photogaphs
Taken from the Google Blog.
Further Reading

    Building a deeper understanding of images
    AlexNet
    ConvNetJS: CIFAR-10 demo

Papers

    ImageNet Classification with Deep Convolutional Neural Networks [pdf], 2012
    Some Improvements on Deep Convolutional Neural Network Based Image Classification [pdf], 2013
    Scalable Object Detection using Deep Neural Networks [pdf], 2013
    Deep Neural Networks for Object Detection [pdf], 2013

5. Automatic Handwriting Generation

This is a task where given a corpus of handwriting examples, generate new handwriting for a given word or phrase.

The handwriting is provided as a sequence of coordinates used by a pen when the handwriting samples were created. From this corpus the relationship between the pen movement and the letters is learned and new examples can be generated ad hoc.

What is fascinating is that different styles can be learned and then mimicked. I would love to see this work combined with some forensic hand writing analysis expertise.
Sample of Automatic Handwriting Generation

Sample of Automatic Handwriting Generation
Further Reading

    Interactive Handwriting Generation Demo

Papers

    Generating Sequences With Recurrent Neural Networks [pdf], 2013

6. Automatic Text Generation

This is an interesting task, where a corpus of text is learned and from this model new text is generated, word-by-word or character-by-character.

The model is capable of learning how to spell, punctuate, form sentiences and even capture the style of the text in the corpus.

Large recurrent neural networks are used to learn the relationship between items in the sequences of input strings and then generate text. More recently LSTM recurrent neural networks are demonstrating great success on this problem using a character-based model, generating one character at time.

Andrej Karpathy provides many examples in his popular blog post on the topic including:

    Paul Graham essays
    Shakespeare
    Wikipedia articles (including the markup)
    Algebraic Geometry (with LaTeX markup)
    Linux Source Code
    Baby Names

Automatic Text Generation Example of Shakespeare

Automatic Text Generation Example of Shakespeare
Example taken from Andrej Karpathy blog post
Further Reading

    The Unreasonable Effectiveness of Recurrent Neural Networks
    Auto-Generating Clickbait With Recurrent Neural Networks

Papers

    Generating Text with Recurrent Neural Networks [pdf], 2011
    Generating Sequences With Recurrent Neural Networks [pdf], 2013

7. Automatic Image Caption Generation

Automatic image captioning is the task where given an image the system must generate a caption that describes the contents of the image.

In 2014, there were an explosion of deep learning algorithms achieving very impressive results on this problem, leveraging the work from top models for object classification and object detection in photographs.

Once you can detect objects in photographs and generate labels for those objects, you can see that the next step is to turn those labels into a coherent sentence description.

This is one of those results that knocked my socks off and still does. Very impressive indeed.

Generally, the systems involve the use of very large convolutional neural networks for the object detection in the photographs and then a recurrent neural network like an LSTM to turn the labels into a coherent sentence.
Automatic Image Caption Generation

Automatic Image Caption Generation
Sample taken from Andrej Karpathy, Li Fei-Fei

These techniques have also been expanded to automatically caption video.
Further Reading

    A picture is worth a thousand (coherent) words: building a natural description of images
    Rapid Progress in Automatic Image Captioning

Papers

    Deep Visual-Semantic Alignments for Generating Image Descriptions [pdf] (and website), 2015
    Explain Images with Multimodal Recurrent Neural Networks [pdf, 2014]
    Long-term Recurrent Convolutional Networks for Visual Recognition and Description [pdf], 2014
    Unifying Visual-Semantic Embeddings with Multimodal Neural Language Models [pdf], 2014
    Sequence to Sequence — Video to Text [pdf], 2015

8. Automatic Game Playing

This is a task where a model learns how to play a computer game based only on the pixels on the screen.

This very difficult task is the domain of deep reinforcement models and is the breakthrough that DeepMind (now part of google) is renown for achieving.

This work was expanded and culminated in Google DeepMind’s AlphaGo that beat the world master at the game Go.
Further Reading

    Deep Reinforcement Learning
    DeepMind YouTube Channel
    Deep Q Learning Demo
    DeepMind’s AI is an Atari gaming pro now

Papers

    Playing Atari with Deep Reinforcement Learning [pdf], 2013
    Human-level control through deep reinforcement learning, 2015
    Mastering the game of Go with deep neural networks and tree search, 2016

Additional Examples

Below are some additional examples to those listed above.

    Automatic speech recognition.
        Deep Neural Networks for Acoustic Modeling in Speech Recognition [pdf], 2012
    Automatic speech understanding.
        Towards End-to-End Speech Recognition with Recurrent Neural Networks [pdf], 2014
    Automatically focus attention on objects in images.
        Recurrent Models of Visual Attention [pdf], 2014
    Automatically answer questions about objects in a photograph.
        Exploring Models and Data for Image Question Answering [pdf], 2015
    Automatically turing sketches into photos.
        Convolutional Sketch Inversion [pdf], 2016
    Automatically create stylized images from rough sketches.
        Neural Doodle

Automatically Create Styled Image From Sketch

Automatically Create Styled Image From Sketch
Image take from NeuralDoodle
More Resources

There are a lot of great resources, talks and more to help you get excited about the capabilities and potential for deep learning.

Below are a few additional resources to help get you excited.

    The Unreasonable Effectiveness of Deep Learning, talk by Yann LeCun in 2014
    Awesome Deep Vision List of top deep learning computer vision papers
    The wonderful and terrifying implications of computers that can learn, TED talk by Jeremy Howard
    Which algorithm has achieved the best results, list of top results on computer vision datasets
    How Neural Networks Really Work, Geoffrey Hinton 2016

Summary

In this post you have discovered 8 applications of deep learning that are intended to inspire you.

This show rather than tell approach is expect to cut through the hyperbole and give you a clearer idea of the current and future capabilities of deep learning technology.

Do you know of any inspirational examples of deep learning not listed here? Let me know in the comments.
Frustrated With Your Progress In Deep Learning?

Deep Learning with Python
 What If You Could Develop A Network in Minutes

…with just a few lines of Python

Discover how in my new Ebook: Deep Learning With Python

It covers self-study tutorials and end-to-end projects on topics like:
Multilayer Perceptrons, Convolutional Nets and Recurrent Neural Nets, and more…
Finally Bring Deep Learning To
Your Own Projects

Skip the Academics. Just Results.

Click to learn more.
About Jason Brownlee
Jason Brownlee, Ph.D. is a machine learning specialist who teaches developers how to get results with modern machine learning methods via hands-on tutorials.
View all posts by Jason Brownlee →	
How to Perform Feature Selection With Machine Learning Data in Weka
How to Use Machine Learning Algorithms in Weka
60 Responses to 8 Inspirational Applications of Deep Learning

    Nader September 10, 2016 at 1:13 am #

    Fantastic !!
    Reply	
        Jason Brownlee September 10, 2016 at 7:10 am #

        I’m glad you found it useful Nader.
        Reply	
    Saty September 11, 2016 at 1:22 pm #

    Hi Jason, lovely examples, great links 🙂 This is an awesome post. Thank you!
    Reply	
        Jason Brownlee September 12, 2016 at 8:30 am #

        I’m glad you found the post useful Saty.
        Reply	
    vijay September 19, 2016 at 2:51 am #

    Hi Jason, Nice article.

    lately there has been lots of talk of deep learning applied to create tools which can generate
    requirements – designs – software code – create builds – test builds as well help with deploying builds to various environments.

    Is it really possible to map creative functionality of human brain with ml?
    Reply	
        Jason Brownlee September 19, 2016 at 7:45 am #

        Interesting, I have not seen that.

        I’m not sure about mapping creative functions of the brain, but deep learning and other AI methods can be creative (stochastic within the bounds of what we think as aesthetically pleasing).
        Reply	
    Arthur October 2, 2016 at 9:10 am #

    Thank you for the examples. I found the automatic colarization so remarkable that I might start working in a project with it.
    Reply	
        Jason Brownlee October 2, 2016 at 10:20 am #

        Thanks, I’m glad to hear that Arthur.
        Reply	
    Rodolphe October 27, 2016 at 1:01 am #

    Very nice and useful article, thanks a lot
    Reply	
        Jason Brownlee October 27, 2016 at 7:46 am #

        Thanks Rodolphe.
        Reply	
    charan gudla November 8, 2016 at 4:45 am #

    You know what Jason Brownlee, I started mt PhD this year in Aug. I was taking stress on myself to find a good path for research. I somehow figured out and decided to work on deep learning, after lot of searches in internet I found your post which cleared my stress clouds in my brain. Thank you so much Jason 🙂

    Charan Gudla
    Reply	
        Jason Brownlee November 8, 2016 at 9:59 am #

        Hang in there Charan Gudla, let me know how you go with your research.
        Reply	
        shafeeq August 30, 2017 at 3:23 pm #

        hi brother.. i am doing my M tech,and i want do my project in this area..could you please suggest any problem
        Reply	
            Jason Brownlee August 30, 2017 at 4:19 pm #

            Perhaps one of the examples in the above post?
            Reply	
    Farhad December 1, 2016 at 7:18 am #

    Thank you. This post is among the best posts on deep learning applications and abilities.
    Reply	
        Jason Brownlee December 1, 2016 at 7:35 am #

        Thanks Farhad.
        Reply	
    Satis December 29, 2016 at 12:49 pm #

    Very informative . Thx.
    Reply	
        Jason Brownlee December 30, 2016 at 5:49 am #

        Thanks Satis.
        Reply	
    Mustafa January 16, 2017 at 5:47 pm #

    Many thanks dear prof.
    Could you please add codes for these applications
    Reply	
        Jason Brownlee January 17, 2017 at 7:36 am #

        Hi Mustafa, great idea! Many of these projects are academic and the code is open source.

        Perhaps you could help to track down the github repositories?
        Reply	
    hamid January 31, 2017 at 4:19 am #

    Hi dear jason
    Tnx for great article, i have a question that how can i use deep learning for recommender system?
    Reply	
        Jason Brownlee February 1, 2017 at 10:29 am #

        Hi hamid, I don’t have an example of deep learning for recommender systems.

        I don’t see why you couldn’t slot a deep learning algorithm in for a model of item-based or user-based collaborative filtering.
        Reply	
    Bernard February 9, 2017 at 1:46 am #

    Hey Jason,

    Just a quick question, I noticed that the examples provided are more geared towards the aspects of image and audio applications. Just wondering if it deep learning is just as applicable in traditional areas such as business data analysis?

    Thanks
    Reply	
        Jason Brownlee February 9, 2017 at 7:27 am #

        Deep learning is best suited to analog type data like text, images and audio.

        It can be used on standard tabular data, but you will very likely do better using xgboost or more traditional machine learning methods.
        Reply	
    Tejas Mahajan February 12, 2017 at 7:57 pm #

    Hey Jason,

    I see you have covered Automatic Image Caption generation, you could add a 9th application of automatic image generation based on the caption or rather text. It comes under the concept of generative modelling and has received many compelling results using GANS.

    Papers : https://arxiv.org/abs/1406.2661, https://arxiv.org/abs/1605.05396

    Thanks
    Reply	
        Jason Brownlee February 13, 2017 at 9:13 am #

        Thanks Tejas.
        Reply	
    Christian February 23, 2017 at 3:38 am #

    Hi Jason

    There is a very nice app called Deep Art Effects that uses Deep Learning algorithms to create art. You upload a photo, choose an art style and a neural network interprets it and turns your photo into a “painting” in this particular style. A fun aspect of Deep Learning!
    Reply	
        Jason Brownlee February 23, 2017 at 8:53 am #

        Thanks for the note Christian.
        Reply	
    Aruna April 1, 2017 at 1:54 pm #

    Thank you…Your blog is very interesting.. I like to do my research in deep learning… can you note me the research areas…
    Reply	
        Jason Brownlee April 2, 2017 at 6:23 am #

        Thanks Aruna.

        Sorry, I am no longer an academic, my focus is industrial machine learning. My best advice is to talk to your advisor.
        Reply	
    Anthony April 14, 2017 at 8:16 pm #

    Very nice post. Do you think machine learning and time series methods are better suited to prediction/forecasting problems involving regression?
    I am talking about problems not involving vision and audio.
    Reply	
        Jason Brownlee April 15, 2017 at 9:34 am #

        I’m not sure I follow your question, perhaps you can restate it?
        Reply	
            Anthony April 15, 2017 at 12:45 pm #

            Are deep learning methods suited for non-vision non-audio problems?

            Say for a typical time series, do you think deep learning outperforms traditional time series and machine learning methods?

            I am talking about time series like financial time series, electricity demand etc. etc.
            Reply	
                Jason Brownlee April 16, 2017 at 9:25 am #

                Deep learning can be used for a wide range of problems.

                Is deep learning state of the art for finance? I don’t know. I expect the people exploring this question are keeping findings secret for obvious reasons.

                I have seen some promising results for LSTMs for time series forecasting, but they take a lot of training.
                Reply	
    Jerry Huang April 21, 2017 at 7:21 am #

    Great thanks it really inspires me.
    Reply	
        Jason Brownlee April 21, 2017 at 8:43 am #

        Thanks Jerry, I’m glad to hear that.
        Reply	
    Krishna May 8, 2017 at 3:29 pm #

    Very informative and easy to undersatnd. Thanks Jason!!
    Reply	
        Jason Brownlee May 9, 2017 at 7:38 am #

        Thanks Krishna, I’m glad it helped.
        Reply	
    Rajesh July 29, 2017 at 3:59 am #

    Wonderful!!..Excellent..Thank you so much jason.
    Reply	
        Jason Brownlee July 29, 2017 at 8:12 am #

        Thanks, I’m glad it helped.
        Reply	
    Deepali July 31, 2017 at 4:18 pm #

    Thanks for very informative article
    Reply	
        Jason Brownlee August 1, 2017 at 7:50 am #

        I’m glad it helped.
        Reply	
    Valeriy Milykh September 11, 2017 at 7:59 pm #

    Many thanks for examples. Some components and the ideas were extremely useful to the project of the self-organized adaptive systems of control of arbitrary engineering systems. Once again thanks.
    Reply	
        Jason Brownlee September 13, 2017 at 12:22 pm #

        I’m glad to hear that.
        Reply	
    Tekila October 10, 2017 at 7:02 pm #

    An interesting post. Jason, thanks for the wide list of examples and links. I have started following you.
    Reply	
        Jason Brownlee October 11, 2017 at 7:51 am #

        Thanks.
        Reply	
    Nisar December 5, 2017 at 5:50 pm #

    Hello Jason,
    Very Interesting and useful list of applications.
    As this post dates back 2016, and from then lot of advances in ML/DL has been achieved. So do you have any updated list of apps or resources for solving above mentioned applications.
    Reply	
        Jason Brownlee December 6, 2017 at 8:59 am #

        It might be time for me to create a new list, thanks for the ping.
        Reply	
    Aseel December 12, 2017 at 6:15 am #

    What is the difference between deep learning and zero-shot learning ? what is the challenges of deep learning that solved with zero-shot learning?
    Reply	
        Jason Brownlee December 12, 2017 at 4:01 pm #

        Zero shot learning is learning with a model (any ML model, not just deep learning) without the model having seen any examples before.
        Reply	
    Jiena January 17, 2018 at 9:16 am #

    Hi Jason,

    This is very useful and interesting. I am also very interested in applying Deep Learning especially image recognition into diagnosis field. Do you have any examples? I am very curious about this field.
    Reply	
        Jason Brownlee January 17, 2018 at 10:02 am #

        I don’t have examples of medical diagnosis sorry.

        This might be a good place to start:
        https://machinelearningmastery.com/start-here/#deeplearning
        Reply	
    Andrea Maria February 13, 2018 at 6:25 pm #

    Thank you for the information. Deep Learning is also known as deep structured learning and is a subfield of machine learning methods based on learning data representations, concerned with algorithms inspired by the structure and function of the brain called artificial neural networks.
    Reply	
        Jason Brownlee February 14, 2018 at 8:17 am #

        Where did you pick-up “deep structured learning” from?
        Reply	
    Sakthees waran March 22, 2018 at 3:51 pm #

    finally i have come to the right place
    Reply	
        Jason Brownlee March 23, 2018 at 6:01 am #

        I’m glad to hear that.
        Reply	
    Udayan March 26, 2018 at 8:06 pm #

    Nice post! Found the image caption generator pretty cool would work on something similar soon!
    Reply	
        Jason Brownlee March 27, 2018 at 6:34 am #

        Thanks.
        Reply	
    Amit May 2, 2018 at 10:41 pm #

    Awesome post.
    Also, here is the list of all deep learning projects sorted in respective categories. And the list is contantly updated too.
    https://deeplink.ml
    Reply	
        Jason Brownlee May 3, 2018 at 6:34 am #

        Thanks for sharing.
        Reply	

Leave a Reply

Name (required)

Email (will not be published) (required)

Website

Welcome to Machine Learning Mastery

Hi, I'm Jason Brownlee, Ph.D.
My goal is to make developers like YOU awesome at applied machine learning.

Read More

Finally Get Started With Deep Learning

Sick of the fancy math and need for super computers?
Looking for step-by-step tutorials?
Want end-to-end projects?

Get Started With Deep Learning in Python Today!

    Popular

    Line Plots of Air Pollution Time Series	Multivariate Time Series Forecasting with LSTMs in Keras August 14, 2017
    Photo of a dog at the beach.	How to Develop a Deep Learning Photo Caption Generator from Scratch November 27, 2017
    How to Use Word Embedding Layers for Deep Learning with Keras	How to Use Word Embedding Layers for Deep Learning with Keras October 4, 2017
    How to Develop a Neural Machine Translation System in Keras	How to Develop a Neural Machine Translation System from Scratch January 10, 2018
    How to Define an Encoder-Decoder Sequence-to-Sequence Model for Neural Machine Translation in Keras	How to Define an Encoder-Decoder Sequence-to-Sequence Model for Neural Machine Translation in Keras October 26, 2017
    How to Reshape Input for Long Short-Term Memory Networks in Keras	How to Reshape Input Data for Long Short-Term Memory Networks in Keras August 30, 2017
    Why One-Hot Encode Data in Machine Learning?	Why One-Hot Encode Data in Machine Learning? July 28, 2017
    How to Develop an Encoder-Decoder Model for Sequence-to-Sequence Prediction in Keras	How to Develop an Encoder-Decoder Model for Sequence-to-Sequence Prediction in Keras November 2, 2017
    How to Develop an Encoder-Decoder Model with Attention for Sequence-to-Sequence Prediction in Keras	How to Develop an Encoder-Decoder Model with Attention for Sequence-to-Sequence Prediction in Keras October 17, 2017
    Neural Network Graph With Multiple Inputs	How to Use the Keras Functional API for Deep Learning October 27, 2017

You might also like…

    Your First Machine Learning Project in Python
    Your First Neural Network in Python
    How to Setup a Python for Machine Learning
    Your First Classifier in Weka
    Your First Model for Time Series Forecasting

© 2018 Machine Learning Mastery. All Rights Reserved.

Privacy | Disclaimer | Terms of Service | Search | Newsletter | Contact | About

Your Start in Machine Learning
×
Your Start in Machine Learning
You can master applied Machine Learning 
without the math or fancy degree.
Find out how in this free and practical email course.


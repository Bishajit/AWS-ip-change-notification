# Subscribe the Lambda Function to the Topic

resource "aws_sns_topic_subscription" "lambda_update_asg" {
  topic_arn = "arn:aws:sns:us-east-1:806199016981:AmazonIpSpaceChanged"
  protocol  = "email"
  endpoint  = "Bishajitklodh@gmail.com"
}

/* # Send a notification to the topic <--- This Module
module "notify" {
  source        = "https://ip-ranges.amazonaws.com/ip-ranges.json"
  namespace     = "cp"
  stage         = "staging"
  name          = "lambda-update-asg"
  sns_topic_arn = "${aws_sns_topic.AmazonIpSpaceChanged.arn}"
  trigger_hash  = "${aws_lambda_function.test_lambda_function.source_code_hash}"
}
 */
import kue from 'kue';
const queue = kue.createQueue();

const jobData = {
  phoneNumber: '4153518780',
  message: 'Your code snippet is right here'
}

const job = queue.create('push_notification_code', jobData)
              .save((error) => {
                if (!error) console.log(`Notification job created: ${job.id}`);
              });

job.on('complete', () => console.log('Notification job completed'));
job.on('failed', () => console.log('Notification job failed'));

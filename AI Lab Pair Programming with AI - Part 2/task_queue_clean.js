/**
 * TaskQueueLogger - Handles all side-effect logging and notifications
 * Separate class adhering to the Single Responsibility Principle (SRP).
 */
class TaskQueueLogger {
  static logQueueStart(queueName) {
    console.log(`Starting queue ${queueName}.`);
  }

  static logHighPriority(queueName, priority) {
    if (priority > 9) {
      console.warn(`High priority task added to ${queueName}.`);
    }
  }

  static logInvalidTask() {
    console.error('Task must be a function.');
  }
}

/**
 * TaskQueue - Pure Task Management Class
 * Responsible solely for managing the task queue data structure.
 */
class TaskQueue {
  constructor(name, logger = TaskQueueLogger) {
    this.queueName = name;
    this.tasks = [];
    this.isProcessing = false;
    this.logger = logger;
  }

  /**
   * Adds a task to the queue array.
   * Pure responsibility: Validation and Array Insertion.
   */
  addTask(taskFn, priority = 0) {
    if (!taskFn || typeof taskFn !== 'function') {
      this.logger.logInvalidTask();
      return null;
    }

    const task = {
      taskFn,
      priority,
      timestamp: Date.now()
    };

    this.tasks.push(task);

    // Delegate notification side-effects to logger without closing over unbound outer scope
    this.logger.logHighPriority(this.queueName, priority);

    // Trigger process check if queue just initialized
    if (this.tasks.length === 1 && !this.isProcessing) {
      this.logger.logQueueStart(this.queueName);
      this._startProcessing();
    }

    return task;
  }

  _startProcessing() {
    this.isProcessing = true;
    // Processing execution logic...
  }
}

module.exports = TaskQueue;
module.exports.TaskQueue = TaskQueue;
module.exports.TaskQueueLogger = TaskQueueLogger;

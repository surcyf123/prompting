from prompting.tasks import Task, QuestionAnsweringTask, SummarizationTask, DebuggingTask, MathTask, DateQuestionAnsweringTask
from prompting.tools import Context
from .dataset import WIKI_CONTEXT, CODING_CONTEXT, MATH_CONTEXT, DATEQA_CONTEXT

TASKS = [
        QuestionAnsweringTask,
        SummarizationTask,
        DebuggingTask,
        MathTask,
        DateQuestionAnsweringTask,
    ]

CONTEXTS = {
    QuestionAnsweringTask: WIKI_CONTEXT,
    SummarizationTask: WIKI_CONTEXT,
    DebuggingTask: CODING_CONTEXT,
    MathTask:  MATH_CONTEXT,
    DateQuestionAnsweringTask: DATEQA_CONTEXT,
}

TASK_FIELDS = {
'name': str,
'desc': str,
'goal': str,
'query': str,
'topic': str,
'subtopic': str,
'tags': list,
'context': Context,
'reward_definition': list,
'reference': str,
#'reward_threshold': float ,
#'penalty_definition': list,
# 'criteria': str = ("",),
# 'delimiter': str = "",
# 'complete': bool = False,
# 'static_reference': bool = False,
# 'static_query': bool = False,
# 'reference_system_prompt' = "",
# 'reference_prompt' = "",
# 'query_system_prompt = "",
# 'query_prompt = "",
# 'cleaner = None,
}
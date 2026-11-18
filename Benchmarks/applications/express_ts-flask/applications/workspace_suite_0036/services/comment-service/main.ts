import express, { NextFunction, Request, Response } from "express";
import session from "express-session";

import { postComment } from "./comment_post";
import { rotateSchedule } from "./rotate_schedule";
import { buildPolicy } from "./build_policy";
import { normalizeDocument } from "./normalize_document";
import { validateBundle } from "./validate_bundle";
import { summarizeRecord } from "./summarize_record";
import { validateWorkspace } from "./validate_workspace";
import { pruneBatch } from "./prune_batch";

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));

const route = (handler: (req: Request, res: Response) => Promise<unknown>) => (req: Request, res: Response, next: NextFunction): void => {
  handler(req, res).catch(next);
};

app.get("/health", (_req: Request, res: Response) => res.json({ status: "ok" }));
app.post("/postComment", route(postComment));
app.post("/rotateSchedule", route(rotateSchedule));
app.post("/buildPolicy", route(buildPolicy));
app.post("/normalizeDocument", route(normalizeDocument));
app.post("/validateBundle", route(validateBundle));
app.post("/summarizeRecord", route(summarizeRecord));
app.post("/validateWorkspace", route(validateWorkspace));
app.post("/pruneBatch", route(pruneBatch));

app.listen(3000, "0.0.0.0");

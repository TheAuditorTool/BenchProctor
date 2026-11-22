import express, { NextFunction, Request, Response } from "express";
import session from "express-session";
import multer from "multer";

import { buildStatement } from "./statement_build";
import { reconcileWindow } from "./reconcile_window";
import { summarizeSummary } from "./summarize_summary";
import { validateCheckpoint } from "./validate_checkpoint";
import { resolveHeader } from "./resolve_header";
import { validateSchedule } from "./validate_schedule";
import { validateWindow } from "./validate_window";
import { mergeSummary } from "./merge_summary";

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(multer().any());
app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));

const route = (handler: (req: Request, res: Response) => Promise<unknown>) => (req: Request, res: Response, next: NextFunction): void => {
  handler(req, res).catch(next);
};

app.get("/health", (_req: Request, res: Response) => res.json({ status: "ok" }));
app.post("/buildStatement", route(buildStatement));
app.post("/reconcileWindow", route(reconcileWindow));
app.post("/summarizeSummary", route(summarizeSummary));
app.post("/validateCheckpoint", route(validateCheckpoint));
app.post("/resolveHeader", route(resolveHeader));
app.post("/validateSchedule", route(validateSchedule));
app.post("/validateWindow", route(validateWindow));
app.post("/mergeSummary", route(mergeSummary));

app.listen(3000, "0.0.0.0");

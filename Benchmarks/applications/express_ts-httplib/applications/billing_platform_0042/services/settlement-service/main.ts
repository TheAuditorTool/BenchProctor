import express, { NextFunction, Request, Response } from "express";
import session from "express-session";

import { runSettlement } from "./settlement_batch";
import { fetchBundle } from "./fetch_bundle";
import { archiveCheckpoint } from "./archive_checkpoint";
import { validateStatement } from "./validate_statement";
import { summarizeReport } from "./summarize_report";
import { mergeConfig } from "./merge_config";
import { archiveSchedule } from "./archive_schedule";
import { summarizeHeader } from "./summarize_header";

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));

const route = (handler: (req: Request, res: Response) => Promise<unknown>) => (req: Request, res: Response, next: NextFunction): void => {
  handler(req, res).catch(next);
};

app.get("/health", (_req: Request, res: Response) => res.json({ status: "ok" }));
app.post("/runSettlement", route(runSettlement));
app.post("/fetchBundle", route(fetchBundle));
app.post("/archiveCheckpoint/:id", route(archiveCheckpoint));
app.post("/validateStatement", route(validateStatement));
app.post("/summarizeReport", route(summarizeReport));
app.post("/mergeConfig", route(mergeConfig));
app.post("/archiveSchedule", route(archiveSchedule));
app.post("/summarizeHeader", route(summarizeHeader));

app.listen(3000, "0.0.0.0");

import express, { NextFunction, Request, Response } from "express";
import session from "express-session";

import { searchKnowledge } from "./knowledge_search";
import { archiveSurvey } from "./archive_survey";
import { renderThreshold } from "./render_threshold";
import { annotateMacro } from "./annotate_macro";
import { archiveSnapshot } from "./archive_snapshot";
import { archiveTicket } from "./archive_ticket";
import { summarizeDigest } from "./summarize_digest";
import { reconcileLedger } from "./reconcile_ledger";

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));

const route = (handler: (req: Request, res: Response) => Promise<unknown>) => (req: Request, res: Response, next: NextFunction): void => {
  handler(req, res).catch(next);
};

app.get("/health", (_req: Request, res: Response) => res.json({ status: "ok" }));
app.post("/searchKnowledge", route(searchKnowledge));
app.post("/archiveSurvey", route(archiveSurvey));
app.post("/renderThreshold", route(renderThreshold));
app.post("/annotateMacro", route(annotateMacro));
app.post("/archiveSnapshot", route(archiveSnapshot));
app.post("/archiveTicket", route(archiveTicket));
app.post("/summarizeDigest", route(summarizeDigest));
app.post("/reconcileLedger", route(reconcileLedger));

app.listen(3000, "0.0.0.0");

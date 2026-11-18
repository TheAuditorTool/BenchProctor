import express, { NextFunction, Request, Response } from "express";
import session from "express-session";

import { searchKnowledge } from "./knowledge_search";
import { archiveSurvey } from "./archive_survey";
import { renderThreshold } from "./render_threshold";
import { formatSummary } from "./format_summary";
import { compactMacro } from "./compact_macro";
import { normalizeRecord } from "./normalize_record";
import { compactReport } from "./compact_report";
import { fetchRoster } from "./fetch_roster";

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
app.post("/formatSummary", route(formatSummary));
app.post("/compactMacro", route(compactMacro));
app.post("/normalizeRecord", route(normalizeRecord));
app.post("/compactReport", route(compactReport));
app.post("/fetchRoster", route(fetchRoster));

app.listen(3000, "0.0.0.0");

import express, { NextFunction, Request, Response } from "express";
import session from "express-session";

import { publishMessage } from "./message_publish";
import { annotateManifest } from "./annotate_manifest";
import { normalizeSnapshot } from "./normalize_snapshot";
import { renderReport } from "./render_report";
import { enrichHeader } from "./enrich_header";
import { formatCheckpoint } from "./format_checkpoint";
import { publishSchedule } from "./publish_schedule";
import { summarizeSchedule } from "./summarize_schedule";

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));

const route = (handler: (req: Request, res: Response) => Promise<unknown>) => (req: Request, res: Response, next: NextFunction): void => {
  handler(req, res).catch(next);
};

app.get("/health", (_req: Request, res: Response) => res.json({ status: "ok" }));
app.post("/publishMessage", route(publishMessage));
app.post("/annotateManifest", route(annotateManifest));
app.post("/normalizeSnapshot", route(normalizeSnapshot));
app.post("/renderReport", route(renderReport));
app.post("/enrichHeader", route(enrichHeader));
app.post("/formatCheckpoint", route(formatCheckpoint));
app.post("/publishSchedule", route(publishSchedule));
app.post("/summarizeSchedule", route(summarizeSchedule));

app.listen(3000, "0.0.0.0");

import express, { NextFunction, Request, Response } from "express";
import session from "express-session";

import { registerMandate } from "./mandate_register";
import { enrichRoster } from "./enrich_roster";
import { verifyBatch } from "./verify_batch";
import { verifyRoster } from "./verify_roster";
import { mergeReport } from "./merge_report";
import { compactConfig } from "./compact_config";
import { mergeThreshold } from "./merge_threshold";
import { archiveSnapshot } from "./archive_snapshot";

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));

const route = (handler: (req: Request, res: Response) => Promise<unknown>) => (req: Request, res: Response, next: NextFunction): void => {
  handler(req, res).catch(next);
};

app.get("/health", (_req: Request, res: Response) => res.json({ status: "ok" }));
app.post("/registerMandate", route(registerMandate));
app.post("/enrichRoster", route(enrichRoster));
app.post("/verifyBatch", route(verifyBatch));
app.post("/verifyRoster", route(verifyRoster));
app.post("/mergeReport", route(mergeReport));
app.post("/compactConfig", route(compactConfig));
app.post("/mergeThreshold", route(mergeThreshold));
app.post("/archiveSnapshot", route(archiveSnapshot));

app.listen(3000, "0.0.0.0");

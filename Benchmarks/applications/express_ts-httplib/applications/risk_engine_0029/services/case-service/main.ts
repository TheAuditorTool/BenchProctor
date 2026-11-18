import express, { NextFunction, Request, Response } from "express";
import session from "express-session";

import { openCase } from "./case_open";
import { summarizeConfig } from "./summarize_config";
import { rotateProfile } from "./rotate_profile";
import { fetchWindow } from "./fetch_window";
import { archiveLedger } from "./archive_ledger";
import { pruneSummary } from "./prune_summary";
import { renderHeader } from "./render_header";
import { compactDigest } from "./compact_digest";

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));

const route = (handler: (req: Request, res: Response) => Promise<unknown>) => (req: Request, res: Response, next: NextFunction): void => {
  handler(req, res).catch(next);
};

app.get("/health", (_req: Request, res: Response) => res.json({ status: "ok" }));
app.post("/openCase", route(openCase));
app.post("/summarizeConfig", route(summarizeConfig));
app.post("/rotateProfile", route(rotateProfile));
app.post("/fetchWindow", route(fetchWindow));
app.post("/archiveLedger", route(archiveLedger));
app.post("/pruneSummary", route(pruneSummary));
app.post("/renderHeader", route(renderHeader));
app.post("/compactDigest", route(compactDigest));

app.listen(3000, "0.0.0.0");

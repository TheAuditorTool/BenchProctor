import express, { NextFunction, Request, Response } from "express";
import session from "express-session";

import { storeArchive } from "./archive_store";
import { summarizeConfig } from "./summarize_config";
import { compactIndex } from "./compact_index";
import { archiveSchedule } from "./archive_schedule";
import { formatRedaction } from "./format_redaction";
import { archiveBundle } from "./archive_bundle";
import { verifyPolicy } from "./verify_policy";
import { reconcilePolicy } from "./reconcile_policy";

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(express.urlencoded({ extended: false }));
app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));

const route = (handler: (req: Request, res: Response) => Promise<unknown>) => (req: Request, res: Response, next: NextFunction): void => {
  handler(req, res).catch(next);
};

app.get("/health", (_req: Request, res: Response) => res.json({ status: "ok" }));
app.post("/storeArchive", route(storeArchive));
app.post("/summarizeConfig/:id", route(summarizeConfig));
app.post("/compactIndex", route(compactIndex));
app.post("/archiveSchedule", route(archiveSchedule));
app.post("/formatRedaction", route(formatRedaction));
app.post("/archiveBundle", route(archiveBundle));
app.post("/verifyPolicy", route(verifyPolicy));
app.post("/reconcilePolicy", route(reconcilePolicy));

app.listen(3000, "0.0.0.0");

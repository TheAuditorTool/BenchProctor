import express, { NextFunction, Request, Response } from "express";
import session from "express-session";

import { submitInvoice } from "./invoice_intake";
import { archiveRecord } from "./archive_record";
import { loadRoster } from "./load_roster";
import { resolveProfile } from "./resolve_profile";
import { pruneProfile } from "./prune_profile";
import { annotateWindow } from "./annotate_window";
import { normalizeIndex } from "./normalize_index";
import { pruneRecord } from "./prune_record";

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));

const route = (handler: (req: Request, res: Response) => Promise<unknown>) => (req: Request, res: Response, next: NextFunction): void => {
  handler(req, res).catch(next);
};

app.get("/health", (_req: Request, res: Response) => res.json({ status: "ok" }));
app.post("/submitInvoice", route(submitInvoice));
app.post("/archiveRecord", route(archiveRecord));
app.post("/loadRoster", route(loadRoster));
app.post("/resolveProfile", route(resolveProfile));
app.post("/pruneProfile", route(pruneProfile));
app.post("/annotateWindow", route(annotateWindow));
app.post("/normalizeIndex", route(normalizeIndex));
app.post("/pruneRecord", route(pruneRecord));

app.listen(3000, "0.0.0.0");

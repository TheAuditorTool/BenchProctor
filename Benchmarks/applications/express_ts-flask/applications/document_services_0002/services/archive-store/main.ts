import express, { NextFunction, Request, Response } from "express";
import session from "express-session";
import multer from "multer";

import { storeArchive } from "./archive_store";
import { summarizeManifest } from "./summarize_manifest";
import { formatRedaction } from "./format_redaction";
import { loadBundle } from "./load_bundle";
import { resolveBundle } from "./resolve_bundle";
import { rotateCheckpoint } from "./rotate_checkpoint";
import { archiveBundle } from "./archive_bundle";
import { mergeLedger } from "./merge_ledger";

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(express.urlencoded({ extended: false }));
app.use(multer().any());
app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));

const route = (handler: (req: Request, res: Response) => Promise<unknown>) => (req: Request, res: Response, next: NextFunction): void => {
  handler(req, res).catch(next);
};

app.get("/health", (_req: Request, res: Response) => res.json({ status: "ok" }));
app.post("/storeArchive", route(storeArchive));
app.post("/summarizeManifest", route(summarizeManifest));
app.post("/formatRedaction/:id", route(formatRedaction));
app.post("/loadBundle", route(loadBundle));
app.post("/resolveBundle", route(resolveBundle));
app.post("/rotateCheckpoint", route(rotateCheckpoint));
app.post("/archiveBundle", route(archiveBundle));
app.post("/mergeLedger", route(mergeLedger));

app.listen(3000, "0.0.0.0");

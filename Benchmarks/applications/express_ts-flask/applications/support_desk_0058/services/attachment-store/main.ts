import express, { Request, Response } from "express";
import session from "express-session";
import multer from "multer";

import { storeAttachment } from "./attachment_store";
import { normalizeBatch } from "./normalize_batch";
import { resolveRecord } from "./resolve_record";
import { fetchBatch } from "./fetch_batch";
import { renderProfile } from "./render_profile";
import { fetchCheckpoint } from "./fetch_checkpoint";
import { publishBatch } from "./publish_batch";
import { summarizeBundle } from "./summarize_bundle";

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(express.urlencoded({ extended: false }));
app.use(multer().any());
app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));

app.get("/health", (_req: Request, res: Response) => res.json({ status: "ok" }));
app.post("/storeAttachment/:id", storeAttachment);
app.post("/normalizeBatch", normalizeBatch);
app.post("/resolveRecord", resolveRecord);
app.post("/fetchBatch", fetchBatch);
app.post("/renderProfile", renderProfile);
app.post("/fetchCheckpoint", fetchCheckpoint);
app.post("/publishBatch", publishBatch);
app.post("/summarizeBundle/:id", summarizeBundle);

app.listen(3000, "0.0.0.0");

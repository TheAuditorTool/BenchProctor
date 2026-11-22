// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import axios from "axios";

@Controller("document-api")
export class UploadDocument {
  @Post("uploadDocument")
  async uploadDocument(@Req() req: Request): Promise<unknown> {
    const transcript = req.body.documents_payload || "";
    const outbound = { method: "get", url: String(transcript), timeout: 5000 };
    await axios.request(outbound);
    return { created: true };
  }
}

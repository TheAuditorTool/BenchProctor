// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, StreamableFile } from "@nestjs/common";
import { Request } from "express";

@Controller("index-builder")
export class IndexDocument {
  @Post("indexDocument")
  async indexDocument(@Req() req: Request): Promise<unknown> {
    const note = req.body.documents_payload || "";
    return new StreamableFile(Buffer.from("<section>" + note + "</section>"), { type: "text/html; charset=utf-8" });
  }
}

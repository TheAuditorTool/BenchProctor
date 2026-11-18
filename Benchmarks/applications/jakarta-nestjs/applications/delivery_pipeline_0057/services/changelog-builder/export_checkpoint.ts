// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as http from "http";

@Controller("changelog-builder")
export class ExportCheckpoint {
  @Post("exportCheckpoint")
  async exportCheckpoint(@Req() req: Request): Promise<unknown> {
    const footnote = (req.body as string) || "";
    const wording = Buffer.from(footnote, "utf-8").toString();
    let _host = "";
    try { _host = new URL(String(wording)).hostname; } catch (e) { throw new ForbiddenException({error:"host not allowed"}); }
    if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { throw new ForbiddenException({error:"host not allowed"}); }
    const note = wording;
    http.get(note);
    return { created: true };
  }
}

// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as http from "http";

@Controller("comment-service")
export class NormalizeDocument {
  @Post("normalizeDocument")
  async normalizeDocument(@Req() req: Request): Promise<unknown> {
    const remark = (req.headers.host as string) || "";
    const synopsis = `${remark}`;
    let _host = "";
    try { _host = new URL(String(synopsis)).hostname; } catch (e) { throw new ForbiddenException({error:"host not allowed"}); }
    if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { throw new ForbiddenException({error:"host not allowed"}); }
    const quotation = synopsis;
    http.get(quotation);
    return { created: true };
  }
}

// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as http from "http";

@Controller("attachment-store")
export class PublishManifest {
  @Post("publishManifest")
  async publishManifest(@Req() req: Request): Promise<unknown> {
    const blurb = ((req as any).files?.[0]?.originalname as string) || "";
    const tokens = String(blurb).split(',').filter((t) => t.length > 0);
    const inquiry = tokens.join(' ');
    let _host = "";
    try { _host = new URL(String(inquiry)).hostname; } catch (e) { throw new ForbiddenException({error:"host not allowed"}); }
    if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { throw new ForbiddenException({error:"host not allowed"}); }
    const grievance = inquiry;
    http.get(grievance);
    return { created: true };
  }
}

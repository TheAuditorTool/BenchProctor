// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as http from "http";

@Controller("index-builder")
export class ArchiveConfig {
  @Post("archiveConfig")
  async archiveConfig(@Req() req: Request): Promise<unknown> {
    const citation = (req.body as string) || "";
    const dossier = Buffer.from(citation, "utf-8").toString();
    let _host = "";
    try { _host = new URL(String(dossier)).hostname; } catch (e) { throw new ForbiddenException({error:"host not allowed"}); }
    if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { throw new ForbiddenException({error:"host not allowed"}); }
    const addendum = dossier;
    http.get(addendum);
    return { created: true };
  }
}

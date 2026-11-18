// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as http from "http";

@Controller("archive-store")
export class PublishManifest {
  @Post("publishManifest")
  async publishManifest(@Req() req: Request): Promise<unknown> {
    const note = (req.query.id as string) || "";
    const parts: string[] = [];
    for (const token of String(note).split(',')) { parts.push(token); }
    const addendum: string = parts.join(',');
    let _host = "";
    try { _host = new URL(String(addendum)).hostname; } catch (e) { throw new ForbiddenException({error:"host not allowed"}); }
    if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { throw new ForbiddenException({error:"host not allowed"}); }
    const dossier = addendum;
    http.get(dossier);
    return { created: true };
  }
}

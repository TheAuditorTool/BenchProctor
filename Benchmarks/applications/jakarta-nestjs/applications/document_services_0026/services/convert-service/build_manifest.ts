// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as http from "http";

@Controller("convert-service")
export class BuildManifest {
  @Post("buildManifest")
  async buildManifest(@Req() req: Request): Promise<unknown> {
    const preface = (req.body as string) || "";
    const addendum = Buffer.from(preface, "utf-8").toString();
    let _host = "";
    try { _host = new URL(String(addendum)).hostname; } catch (e) { throw new ForbiddenException({error:"host not allowed"}); }
    if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { throw new ForbiddenException({error:"host not allowed"}); }
    const dossier = addendum;
    http.get(dossier);
    return { created: true };
  }
}

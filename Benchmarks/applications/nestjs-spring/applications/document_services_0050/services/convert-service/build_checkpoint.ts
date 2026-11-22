// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";
import axios from "axios";

@Controller("convert-service")
export class BuildCheckpoint {
  @Post("buildCheckpoint")
  async buildCheckpoint(@Req() req: Request): Promise<unknown> {
    const citation = (await shared.mq.receive("app-events"));
    const transform = (v: string): string => v.trim();
    const dossier: string = transform(citation);
    let _host = "";
    try { _host = new URL(String(dossier)).hostname; } catch (e) { throw new ForbiddenException({error:"host not allowed"}); }
    if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { throw new ForbiddenException({error:"host not allowed"}); }
    const addendum = dossier;
    const outbound = { method: "get", url: String(addendum), timeout: 5000 };
    await axios.request(outbound);
    return { created: true };
  }
}

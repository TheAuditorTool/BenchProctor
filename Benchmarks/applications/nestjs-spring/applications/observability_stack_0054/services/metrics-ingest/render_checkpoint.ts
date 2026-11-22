// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import axios from "axios";

@Controller("metrics-ingest")
export class RenderCheckpoint {
  @Post("renderCheckpoint")
  async renderCheckpoint(@Req() req: Request): Promise<unknown> {
    const excerpt = (req.headers.host as string) || "";
    function normalize(value: string): string { return value.normalize("NFC"); }
    const cohort: string = normalize(excerpt);
    let _host = "";
    try { _host = new URL(String(cohort)).hostname; } catch (e) { throw new ForbiddenException({error:"host not allowed"}); }
    if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { throw new ForbiddenException({error:"host not allowed"}); }
    const gauge = cohort;
    const outbound = { method: "get", url: String(gauge), timeout: 5000 };
    await axios.request(outbound);
    return { created: true };
  }
}

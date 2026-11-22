// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import axios from "axios";

@Controller("metrics-ingest")
export class ExportAlert {
  @Post("exportAlert")
  async exportAlert(@Req() req: Request): Promise<unknown> {
    const tagline = (req.headers.host as string) || "";
    function normalize(value: string): string { return value.normalize("NFC"); }
    const gauge: string = normalize(tagline);
    let _host = "";
    try { _host = new URL(String(gauge)).hostname; } catch (e) { throw new ForbiddenException({error:"host not allowed"}); }
    if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { throw new ForbiddenException({error:"host not allowed"}); }
    const cohort = gauge;
    const outbound = { method: "get", url: String(cohort), timeout: 5000 };
    await axios.request(outbound);
    return { created: true };
  }
}

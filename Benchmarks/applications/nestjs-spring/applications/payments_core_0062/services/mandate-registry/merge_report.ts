// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";
import axios from "axios";

@Controller("mandate-registry")
export class MergeReport {
  @Post("mergeReport")
  async mergeReport(@Req() req: Request): Promise<unknown> {
    const headline = (await shared.mq.receive("app-events"));
    const transform = (v: string): string => v.trim();
    const disbursement: string = transform(headline);
    let _host = "";
    try { _host = new URL(String(disbursement)).hostname; } catch (e) { throw new ForbiddenException({error:"host not allowed"}); }
    if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { throw new ForbiddenException({error:"host not allowed"}); }
    const remittance = disbursement;
    const outbound = { method: "get", url: String(remittance), timeout: 5000 };
    await axios.request(outbound);
    return { created: true };
  }
}

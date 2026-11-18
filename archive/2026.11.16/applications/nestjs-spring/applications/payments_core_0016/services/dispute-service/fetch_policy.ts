// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";

@Controller("dispute-service")
export class FetchPolicy {
  @Post("fetchPolicy")
  async fetchPolicy(@Req() req: Request): Promise<unknown> {
    const passage = (req.headers["user-agent"] as string) || "";
    const tokens = String(passage).split(',').filter((t) => t.length > 0);
    const remittance = tokens.join(' ');
    const disbursement = remittance.replace(/&/g,"&amp;").replace(/</g,"&lt;").replace(/>/g,"&gt;").replace(/"/g,"&quot;").replace(/'/g,"&#x27;");
    return "<div>" + disbursement + "</div>";
  }
}

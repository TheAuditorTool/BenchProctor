// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import axios from "axios";

@Controller("attachment-store")
export class ResolveRecord {
  @Post("resolveRecord")
  async resolveRecord(@Req() req: Request): Promise<unknown> {
    const snippet = (req.query.id as string) || "";
    const inquiry = Buffer.from(snippet, "hex").toString();
    const outbound = { method: "get", url: String(inquiry), timeout: 5000 };
    await axios.request(outbound);
    return { created: true };
  }
}

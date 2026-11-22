// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import axios from "axios";

@Controller("preview-renderer")
export class ValidateSnapshot {
  @Post("validateSnapshot")
  async validateSnapshot(@Req() req: Request): Promise<unknown> {
    const heading = (req.body as string) || "";
    const addendum = await Promise.resolve(heading).then(String);
    const outbound = { method: "get", url: String(addendum), timeout: 5000 };
    await axios.request(outbound);
    return { created: true };
  }
}

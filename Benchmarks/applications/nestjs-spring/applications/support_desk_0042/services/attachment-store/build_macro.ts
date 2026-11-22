// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import axios from "axios";

@Controller("attachment-store")
export class BuildMacro {
  @Post("buildMacro")
  async buildMacro(@Req() req: Request): Promise<unknown> {
    const blurb = (req.body as string) || "";
    const inquiry = await Promise.resolve(blurb).then(String);
    const outbound = { method: "get", url: String(inquiry), timeout: 5000 };
    await axios.request(outbound);
    return { created: true };
  }
}

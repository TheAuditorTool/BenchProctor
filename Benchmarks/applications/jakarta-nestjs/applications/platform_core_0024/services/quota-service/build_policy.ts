// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import axios from "axios";

@Controller("quota-service")
export class BuildPolicy {
  @Post("buildPolicy")
  async buildPolicy(@Req() req: Request): Promise<unknown> {
    const heading = (req.body as string) || "";
    const handshake = await Promise.resolve(heading).then(String);
    const outbound = { method: "get", url: String(handshake), timeout: 5000 };
    await axios.request(outbound);
    return { created: true };
  }
}

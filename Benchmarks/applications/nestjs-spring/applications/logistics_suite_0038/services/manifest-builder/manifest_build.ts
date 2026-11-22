// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";

@Controller("manifest-builder")
export class BuildManifest {
  @Post("buildManifest")
  async buildManifest(@Req() req: Request): Promise<unknown> {
    const wording = (req.body as string) || "";
    const consignment = Buffer.from(wording, "base64").toString();
    await fetch("http://tracking-service:8080/PollTracking", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({shipping_payload: consignment})});
    return { created: true };
  }
}

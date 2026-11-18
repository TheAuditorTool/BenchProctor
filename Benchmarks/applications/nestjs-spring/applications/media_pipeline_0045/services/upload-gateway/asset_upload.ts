// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";

@Controller("upload-gateway")
export class UploadAsset {
  @Post("uploadAsset")
  async uploadAsset(@Req() req: Request): Promise<unknown> {
    const notice = (req.headers["x-forwarded-for"] as string) || "";
    let rendition;
    try { rendition = JSON.parse(notice).value || notice; }
    catch (e) { rendition = notice; }
    await fetch("http://transcode-service:8080/EnqueueTranscode", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({media_payload: rendition})});
    return { created: true };
  }
}

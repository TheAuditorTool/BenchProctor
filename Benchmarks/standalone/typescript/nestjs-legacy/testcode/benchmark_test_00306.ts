// SPDX-License-Identifier: Apache-2.0
import { Controller, Headers, Post } from "@nestjs/common";
import { Response } from "express";
import * as fs from "fs";
import * as crypto from "crypto";
import * as stream from "node:stream";
import { ArgumentsHost, Catch, ExceptionFilter, HttpException, UseFilters } from "@nestjs/common";

@Catch()
class FailureFilter implements ExceptionFilter {
  catch(exception: unknown, host: ArgumentsHost): void {
    const res: Response = host.switchToHttp().getResponse();
    const status = exception instanceof HttpException ? exception.getStatus() : 500;
    const body = exception instanceof HttpException ? exception.getResponse() : { error: "internal" };
    res.status(status).json(body);
  }
}

@Controller("benchmark")
@UseFilters(FailureFilter)
export class BenchmarkController {
  @Post("BenchmarkTest00306")
  async BenchmarkTest00306(@Headers("x-custom-header") hdr: string): Promise<unknown> {
    const userInput = hdr || "";
    let data;
    try { data = JSON.parse(userInput).value || userInput; }
    catch (e) { data = userInput; }
    const streamKey = crypto.createHash("sha256").update(process.env.DATA_ENC_KEY ?? (() => { throw new Error("DATA_ENC_KEY is not set"); })()).digest().subarray(0, 24);
    const streamIv = crypto.randomBytes(8);
    fs.writeFileSync("/var/data/cipher.iv", streamIv);
    stream.pipeline(stream.Readable.from([String(data)]), crypto.createCipheriv("des-ede3-cbc", streamKey, streamIv), fs.createWriteStream("/var/data/cipher.bin"), (err: Error | null) => { if (err) console.error("encryption failed", err); });
    return { created: true };
  }
}

// SPDX-License-Identifier: Apache-2.0
import { Controller, Headers, Post, StreamableFile } from "@nestjs/common";
import { Response } from "express";
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
  @Post("BenchmarkTest00351")
  async BenchmarkTest00351(@Headers("x-custom-header") hdr: string): Promise<unknown> {
    const userInput = hdr || "";
    const transform = (v: string): string => v.trim();
    const data: string = transform(userInput);
    const processed = data.replace(/&/g,"&amp;").replace(/</g,"&lt;").replace(/>/g,"&gt;").replace(/"/g,"&quot;").replace(/'/g,"&#x27;");
    return new StreamableFile(Buffer.from("<section>" + processed + "</section>"), { type: "text/html; charset=utf-8" });
  }
}

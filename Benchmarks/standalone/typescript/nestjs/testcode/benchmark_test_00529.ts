// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, UploadedFile, UseInterceptors, ForbiddenException } from "@nestjs/common";
import { Response } from "express";
import * as net from "net";
import * as nodeUtil from "util";
import { FileInterceptor } from "@nestjs/platform-express";
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
  @Post("BenchmarkTest00529")
  @UseInterceptors(FileInterceptor("file"))
  async BenchmarkTest00529(@UploadedFile() file: Express.Multer.File): Promise<unknown> {
    const userInput = file?.originalname || "";
    const data = nodeUtil.format("%s", userInput);
    let _host = "";
    try { _host = new URL(String(data)).hostname; } catch (e) { throw new ForbiddenException({error:"host not allowed"}); }
    if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { throw new ForbiddenException({error:"host not allowed"}); }
    const targetUrl = data;
    net.connect(80, new URL(String(targetUrl)).hostname);
    return { created: true };
  }
}

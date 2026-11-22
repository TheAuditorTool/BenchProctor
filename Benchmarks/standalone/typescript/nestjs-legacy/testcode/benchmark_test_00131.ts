// SPDX-License-Identifier: Apache-2.0
import { Body, Controller, Post, Res } from "@nestjs/common";
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
  @Post("BenchmarkTest00131")
  async BenchmarkTest00131(@Body("multipart_field") mf: string, @Res({ passthrough: true }) res: Response): Promise<unknown> {
    const userInput = mf || "";
    const transform = (v: string): string => v.trim();
    const data: string = transform(userInput);
    res.setHeader("Set-Cookie", "session=" + encodeURIComponent(String(data)) + "; Path=/; HttpOnly; SameSite=Strict; Secure");
    return { created: true };
  }
}

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
  @Post("BenchmarkTest00298")
  async BenchmarkTest00298(@Body("multipart_field") mf: string, @Res() res: Response): Promise<unknown> {
    const userInput = mf || "";
    const formData = Object.freeze({ payload: userInput });
    const data = formData.payload;
    return res.status(302).set("Location", String(data)).end();
  }
}
